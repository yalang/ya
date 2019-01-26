#!/usr/bin/env bash

# Variable

COMMAND=ya
COMMAND_AR=ي

# Creating a link to local bin so that we do not required to add class path
cp $PWD/bin/cmd.sh bin/${COMMAND}
chmod +x  $PWD/bin/${COMMAND}

rm -f /usr/local/bin/${COMMAND}
rm -f /usr/local/bin/${COMMAND_AR}

ln -s $PWD/bin/${COMMAND} /usr/local/bin/${COMMAND}
ln -s $PWD/bin/${COMMAND} /usr/local/bin/${COMMAND_AR}

echo "Installation successful"
echo "التثبيت بنجاح"