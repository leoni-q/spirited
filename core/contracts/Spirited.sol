// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract Spirited is ERC721 {
    using Strings for string;

    AggregatorV3Interface internal priceFeed;

    string[] public tokenURIs;
    string[] public tokens;

    constructor(address AggregatorAddress) public ERC721("Spirited", "SPR") {
        priceFeed = AggregatorV3Interface(AggregatorAddress);
    }

    function mintToken(string memory name) internal {
        uint256 newId = tokens.length;

        tokens.push(name);
        _safeMint(_msgSender(), newId);
    }

    function changeTokenURIBasedOnEthPrice(uint256 tokenId) internal {
        (
            uint80 roundID,
            int price,
            uint startedAt,
            uint timeStamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();

        if (price % 2 != 0) {
            setTokenURI(tokenId, tokenURIs[0]);
        } else {
            setTokenURI(tokenId, tokenURIs[1]);
        }
    }

    function getTokenURI(uint256 tokenId) public view returns (string memory) {
        return tokenURI(tokenId);
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) internal {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner nor approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
