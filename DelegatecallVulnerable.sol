// Delegatecall Vulnerability Example
pragma solidity ^0.8.28;

contract DelegatecallVulnerable {
    function execute(address _target, bytes memory _data) public {
        _target.delegatecall(_data); // ⚠️ Delegatecall to external contract
    }
}