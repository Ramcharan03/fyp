// Unprotected Initialization Example
pragma solidity ^0.8.28;

contract UnprotectedInit {
    address public owner;

    function init(address _owner) public {
        owner = _owner; // ⚠️ Anyone can change contract owner
    }
}
