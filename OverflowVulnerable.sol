// Integer Overflow Example
pragma solidity ^0.8.28;

contract OverflowVulnerable {
    uint8 public balance = 255; // Max uint8 value

    function increment() public {
        balance += 1; // ⚠️ Vulnerability: Overflow occurs here
    }
}
