# model variations available for keys

## Three-server model
1. On TES startup send request to config server and get back a key. also store key on config server.
2. On TES store key as variable. do not start trading without this var.
3. On Opto server startup also request key from config server, and store in mem in both places.
4. Also on opto server retrieve key for TES from config server to store in mem, use for comms with TES server.

- config server can also be responsible for starting/restarting TES and Opto servers in event of something going down
- config can be a sleepy host that is woken up if it needs to hold optimization vars
- enables messaging queue architecture and parallelization of opto systems trhough 

## Two-server model
1. On TES startup generate a key, have a function that can send key exactly once by setting a state var to false
2. On Opto startup generate a key and have a function that can send the key exactly once.
3. Have opto retrieve key from TES on startup and vice-versa

- opto server must stay awake or at least retain key variable through restart
