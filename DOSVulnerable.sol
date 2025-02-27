// DoS with Gas Limit Example
pragma solidity ^0.8.28;

contract DOSVulnerable {
    address[] public users;

    function addUsers(address _user) public {
        users.push(_user);
    }

    function payout() public {
        for (uint256 i = 0; i < users.length; i++) {
            payable(users[i]).transfer(1 ether); // ⚠️ Gas-intensive loop may fail
        }
    }
}
