@echo off
echo === Cliente 1 ===
curl http://127.0.0.1:5000/rpc_call/hola1
echo.

echo === Cliente 2 ===
curl http://127.0.0.1:5000/rpc_call/hola2
echo.

echo === Cliente 3 ===
curl http://127.0.0.1:5000/rpc_call/hola3
echo.

pause
