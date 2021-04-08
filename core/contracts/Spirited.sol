pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract Spirited is ERC721, Ownable {
    using Strings for string;

    AggregatorV3Interface private priceFeed;

    bytes32[] names;

    mapping(uint => bytes32[12]) idToTokenURIs;
    mapping(uint => string) tokenIdToName;

    constructor(address _priceFeedAddress, bytes32[] memory _initialTokenURIs) public ERC721("Spirited", "SPR") {
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
        uint id;
        uint tokenURIOrdinal;
        for (uint i = 1; i <= _initialTokenURIs.length; i++) {
            idToTokenURIs[id][tokenURIOrdinal] = _initialTokenURIs[i - 1];
            tokenURIOrdinal++;
            if (i % 12 == 0) {
                id++;
                tokenURIOrdinal = 0;
            }
        }
    }

    function getInitialTokenURIs(uint _id) external view returns (bytes32[12] memory) {
        return idToTokenURIs[_id];
    }

    function mintToken(bytes32 _name) external onlyOwner {
        uint256 newId = names.length;
        names.push(_name);
        _safeMint(_msgSender(), newId);
    }

    function changeTokenURIBasedOnBtcPrice(uint _tokenId) external onlyOwner {
        int price;
        (, price,,,) = priceFeed.latestRoundData();
        _setTokenUriByBtcPrice(uint(price), _tokenId);
    }

    function getTokenURI(uint256 tokenId) public view returns (string memory) {
        return tokenURI(tokenId);
    }

    function _setTokenUriByBtcPrice(uint _btcPrice, uint _tokenId) private {
        uint tokenURIOrdinal = _getTokenURIOrdinal(_btcPrice);
        _setTokenURI(_tokenId, string(abi.encodePacked(idToTokenURIs[_tokenId][tokenURIOrdinal])));
    }

    function _getTokenURIOrdinal(uint _btcPrice) private pure returns (uint) {
        uint ordinal;
        if (_btcPrice < 50 * 10 ** 11) {
            return 0;
        } else if (_btcPrice >= 100 * 10 ** 11) {
            return 11;
        } else {
            uint firstTwoDigitsOfBtcPrice = _btcPrice / 10 ** 11;
            uint roundedAndMultiplied = _roundUpToDivisionOfFive(firstTwoDigitsOfBtcPrice) * 2;
            return roundedAndMultiplied / 10 % 10;
        }
    }

    function _roundUpToDivisionOfFive(uint _n) private pure returns (uint) {
        return (_n + 4) / 5 * 5;
    }
}

