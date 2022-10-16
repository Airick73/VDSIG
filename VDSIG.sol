
pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 */
contract VDSIG {

    uint8 public number_of_authentication_data;
    uint public symSignId;
    uint public assymSignId;
    address owner;

    struct Company {
        company_authenticated_data[] company_data;
        string email;
        string name;
        string password;
        string public_key;
        bool set;
    }

    struct User {
        authentication_data data;
        string email;
        string password;
        bool set;
    }

    struct company_authenticated_data{
        authentication_data data;
        string encrypted_key;
    }

    struct authentication_data{
        address owner;        
        string ipfsId;
    }
    
    struct Sign {
        uint symSignId;
        uint assymSignId;
        string key_hash;
        string file_hash;
        string public_key;
    }
    
    mapping(address => Company) public companies;
    mapping(address => User) public users;
    mapping(string => authentication_data) public list_data_ipfs_based;
    mapping(uint8 => authentication_data) public list_data_index_based;
    mapping(string => Sign) public listOfSign;
    mapping(string => Company) public list_companies;
    

    constructor () public{
        owner = msg.sender;

    }
    
    event notify_grant (
        string ipfsId,
        string encrypted_key,
        string public_key
        );

    // event sendPublicKey (
    //     string ipfsId,
    //     string publicKey,
    //     address sellerId
    //     );
        

    function stringToBytes32 (string memory source) private returns (bytes32 result) {
        bytes memory tempEmptyStringTest = bytes(source);
        if (tempEmptyStringTest.length == 0) {
            return 0x0;
        }

        assembly {
            result := mload(add(source, 32))
        }
    }
    
    
    function create_user( string memory email,string memory password) public {
        User storage user = users[msg.sender];
        // Check that the user did not already exist:
        require(!user.set);
        user.email = email;
        user.password = password;
        user.set = true;
}

    function create_company( string memory email,string memory name,string memory password,string memory public_key) public {
        Company storage company = companies[msg.sender];
        
        // Check that the user did not already exist:
        require(!company.set);
        company.email = email;
        company.name = name;
        company.password = password;
        company.public_key = public_key;
        company.set = true;
        list_companies[name] = company;
}


    // function getName() public view returns (string memory)
    // {
    //     return name;
    // }

    function add_information(string memory ipfsId) public payable   {
        authentication_data memory data;
        data.ipfsId = ipfsId;
        data.owner = msg.sender;
        list_data_ipfs_based[ipfsId] = data;
        list_data_index_based[number_of_authentication_data] = data;
        users[msg.sender].data = data;
        number_of_authentication_data += 1;
    }


    function grant_access(string memory company_name,string memory encrypted_key) public payable {
        company_authenticated_data memory company_data;
        company_data.data = users[msg.sender].data;
        company_data.encrypted_key = encrypted_key;
        list_companies[company_name].company_data.push(company_data);
        emit notify_grant(users[msg.sender].data.ipfsId,encrypted_key,list_companies[company_name].public_key);
    }
}