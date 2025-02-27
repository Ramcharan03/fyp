// Hardcoded Private Key Example
pragma solidity ^0.8.28;

contract HardcodedKey {
    string private key = "my_secret_key"; // ⚠️ This key is exposed in contract storage

    function getKey() public view returns (string memory) {
        return key;
    }
}
