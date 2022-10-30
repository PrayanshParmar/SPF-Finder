#include <iostream>
#include<string> 

#include "modes.h" 
#include "aes.h"
#include "cryptlib.h"  
using namespace CryptoPP;
using namespace std;


int main() 
{
  CryptoPP::byte key[] = "qwertyuiopasdfg"; 
  size_t k_size = sizeof(key);  
  CryptoPP::byte iv[] = "qwertyuiopasdfg";
  string plain = "CBC Mode Test";
  string cipher, encoded, recovered; 
  try
  {
    cout << "plain text: " << plain << endl; 

    CBC_Mode<AES>::Encryption e;
    e.SetKeyWithIV(&key[0], k_size, &iv[0]); 
    // The StreamTransformationFilter adds padding
    //  as required. ECB and CBC Mode must be padded
    //  to the block size of the cipher.
    // convert plain text into cipher text
    StringSource ss(plain, true, new StreamTransformationFilter(e, new StringSink(cipher))); 
  }
  catch (const CryptoPP::Exception &e)
  {
    cerr << e.what() << endl;
    exit(1); 
  }
  cout << "cipher text: " << cipher << endl; 
  
  
  try
  {
    CBC_Mode< AES >::Decryption d; 
    d.SetKeyWithIV(&key[0], k_size, &iv[0]);

    // The StreamTransformationFilter removes
    // padding as required.
    // convert cipher text into plain text
    StringSource ss( cipher, true, 
        new StreamTransformationFilter( d,
            new StringSink( recovered )
        ) 
    );

    cout << "recovered text: " << recovered << endl; 
  }
  catch( const CryptoPP::Exception& e )
  {
  {
    cerr << e.what() << endl;
    exit(1);
  }  

}
