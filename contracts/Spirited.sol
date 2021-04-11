pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract Spirited is ERC721, Ownable {
    using Strings for string;

    string constant ipfsUrl = "https://ipfs.io/ipfs/";

    AggregatorV3Interface private priceFeed;

    bytes32[] names;

    mapping(uint => string[7]) idToTokenURIHashes;
    mapping(uint => string) tokenIdToName;

    /// @param _priceFeedAddress - address of chainlink btc_usd contract.
    constructor(address _priceFeedAddress) public ERC721("Spirited", "SPR") {
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    /// @dev add initial tokenURI hash to indicate the ipfs address hash of an digital artwork
    /// @param _tokenId - token which is going to be linked with given tokenURI hash
    /// @param _position - position at which hash is going to be placed in idToTokenURIHashes mapping
    /// @param _tokenURIHash - hash indicating the ipfs address of digital artwork
    function addInitialTokenURIHash(uint _tokenId, uint _position, string memory _tokenURIHash) external onlyOwner {
        idToTokenURIHashes[_tokenId][_position] = _tokenURIHash;
    }

    function getInitialTokenURIHash(uint _tokenId, uint _position) external view returns (string memory) {
        return idToTokenURIHashes[_tokenId][_position];
    }

    function mintToken(bytes32 _name) external onlyOwner {
        uint256 newId = names.length;
        names.push(_name);
        _safeMint(_msgSender(), newId);
        _setTokenURI(newId, string(abi.encodePacked(ipfsUrl, idToTokenURIHashes[newId][0])));
    }

    /// @dev call this function in order to change tokenURI depending on the btc price provided by chainlink oracle
    /// @param _tokenId - token which price is going to be changed
    function changeTokenURIBasedOnBtcPrice(uint _tokenId) external onlyOwner {
        int price;
        (, price,,,) = priceFeed.latestRoundData();
        _setTokenUriByBtcPrice(uint(price), _tokenId);
    }

    function _setTokenUriByBtcPrice(uint _btcPrice, uint _tokenId) private {
        uint tokenURIOrdinal = _getTokenURIHashOrdinal(_btcPrice);
        _setTokenURI(_tokenId, string(abi.encodePacked(ipfsUrl, idToTokenURIHashes[_tokenId][tokenURIOrdinal])));
    }

    /// @dev get position of a hash in idToTokenURIHashes mapping, to which tokenURI is going to be changed
    function _getTokenURIHashOrdinal(uint _btcPrice) private pure returns (uint) {
        if (_btcPrice < 50 * 10 ** 11) {
            return 0;
        } else if (_isPriceWithin(_btcPrice, 50, 60)) {
            return 1;
        } else if (_isPriceWithin(_btcPrice, 60, 70)) {
            return 2;
        } else if (_isPriceWithin(_btcPrice, 70, 80)) {
            return 3;
        } else if (_isPriceWithin(_btcPrice, 80, 90)) {
            return 4;
        } else if (_isPriceWithin(_btcPrice, 90, 100)) {
            return 5;
        } else if (_btcPrice >= 100 * 10 ** 11) {
            return 6;
        } else {
            return 0;
        }
    }

    /// @dev check if bitcoin price is between given numbers
    function _isPriceWithin(uint _btcPrice, uint _from, uint _to) private pure returns (bool) {
        return _btcPrice >= _from * 10 ** 11 && _btcPrice < _to * 10 ** 11;
    }
}
