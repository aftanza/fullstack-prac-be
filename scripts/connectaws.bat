@echo off

pushd %~dp0
set KEY_PATH=..\AWS\MyKeyPair.pem
set EC2_ADDRESS=ec2-54-251-16-161.ap-southeast-1.compute.amazonaws.com
set EC2_USERNAME=ubuntu

echo Connecting to EC2 instance...

ssh -i "%KEY_PATH%" %EC2_USERNAME%@%EC2_ADDRESS%
if %ERRORLEVEL% neq 0 pause
popd