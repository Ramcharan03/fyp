// Predictable RNG Example
pragma solidity ^0.8.28;

contract PredictableRNG {
    function random() public view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))); // ⚠️ Predictable RNG
    }
}
