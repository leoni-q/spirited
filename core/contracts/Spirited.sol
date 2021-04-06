pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract Spirited is ERC721, Ownable {
    using Strings for string;

    AggregatorV3Interface private priceFeed;

    uint thousandDollarsZerosCount = 10 ** 11;

    bytes32[] names;

    mapping(uint => bytes32[12]) idToTokenURIs;
    mapping(uint => string) tokenIdToName;
    mapping(uint => uint) btcPriceToTokenURIOrdinal;

    constructor(address _priceFeedAddress, bytes32[] memory _initialTokenURIs) public ERC721("Spirited", "SPR") {
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
        uint id = 0;
        for (uint i; i < _initializeTokenURIs.length; i++) {
            idToTokenURIs[id].push(_initializeTokenURIs[i]);
            if (i == 11) {
                id++;
            }
        }
    }

    function mintToken(bytes32 memory _name) external onlyOwner {
        uint256 newId = names.length;
        names.push(_name);
        _safeMint(_msgSender(), newId);
    }

    function changeTokenURIBasedOnBtcPrice(uint _tokenId) external onlyOwner {
        uint price;
        (,price,,,,) = priceFeed.latestRoundData();
        _setTokenUriByBtcPrice(price, _tokenId);
    }

    function getTokenURI(uint256 tokenId) public view returns (string memory) {
        return tokenURI(tokenId);
    }

    function _setTokenUriByBtcPrice(uint _btcPrice, uint _tokenId) private {
        if (_btcPrice < 50000 * thousandDollarsZerosCount) {
            _setTokenURI(_tokenId, tokenURIs[0]);
        } else if (_isPriceWithin(_btcPrice, 50, 55)) {
            _setTokenURI(_tokenId, tokenURIs[1]);
        } else if (_isPriceWithin(_btcPrice, 55, 60) {
            _setTokenURI(_tokenId, tokenURIs[2]);
        } else if (_isPriceWithin(_btcPrice, 60, 65) {
            _setTokenURI(_tokenId, tokenURIs[3]);
        } else if (_isPriceWithin(_btcPrice, 65, 70) {
            _setTokenURI(_tokenId, tokenURIs[4]);
        } else if (_isPriceWithin(_btcPrice, 70, 75) {
            _setTokenURI(_tokenId, tokenURIs[5]);
        } else if (_isPriceWithin(_btcPrice, 75, 80) {
            _setTokenURI(_tokenId, tokenURIs[6]);
        } else if (_isPriceWithin(_btcPrice, 80, 85) {
            _setTokenURI(_tokenId, tokenURIs[7]);
        } else if (_isPriceWithin(_btcPrice, 85, 90) {
            _setTokenURI(_tokenId, tokenURIs[8]);
        } else if (_isPriceWithin(_btcPrice, 90, 95) {
            _setTokenURI(_tokenId, tokenURIs[9]);
        } else if (_isPriceWithin(_btcPrice, 95, 100) {
            _setTokenURI(_tokenId, tokenURIs[10]);
        } else if (_btcPrice > 100 * thousandDollarsZerosCount) {
            _setTokenURI(_tokenId, tokenURIs[11]);
        } else {}
    }

    function _isPriceWithin(uint _price, uint _from, uint _to) pure returns (bool) {
        return _price >= _from * thousandDollarsZerosCount && price < _to * thousandDollarsZerosCount;
    }
}
