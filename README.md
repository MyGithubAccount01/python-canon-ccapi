# Python Library for Canon CCAPI

This library is designed to be a comprehensive library to communicate with Canon cameras via the CCAPI built-in. 

## Adding Endpoints to the Library

A practical rule for adding endpoints
I'd use this decision process every time you add one:
1. Does the endpoint exist in multiple CCAPI versions?
   
   If not, implement only the version that exists.
2. Does its response differ between versions?
   
   If yes, use separate version-specific wire models.
3. Do you need one consistent representation across versions?
   
   If yes, add a normalized model and normalizer.
4. Does the server need to expose this endpoint?
   
   Implement the corresponding server handler and make discovery advertise it.
5. Add tests.
   
   Test parsing the response, client behavior, and server response as appropriate.