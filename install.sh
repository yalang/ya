#!/usr/bin/env bash
# Variable
PROJECT=ya
COMMAND=ya
COMMAND_AR=ي


# Removing existing installation
rm -rf $HOME/${PROJECT}
rm -f /usr/local/bin/${COMMAND}
rm -f /usr/local/bin/${COMMAND_AR}

# Creating directory
mkdir $HOME/${PROJECT}
mkdir $HOME/${PROJECT}/bin
mkdir $HOME/${PROJECT}/src

# Copying file to the directory
cp -r bin/* $HOME/${PROJECT}/bin
cp -r src/* $HOME/${PROJECT}/src
cp start.py $HOME/${PROJECT}


# Renaming command file
mv $HOME/${PROJECT}/bin/cmd.sh $HOME/${PROJECT}/bin/${COMMAND}
chmod +x  $HOME/${PROJECT}/bin/${COMMAND}
# Creating a link to local bin so that we do not required to add class path
ln -s $HOME/${PROJECT}/bin/${COMMAND} /usr/local/bin/${COMMAND}
ln -s $HOME/${PROJECT}/bin/${COMMAND} /usr/local/bin/${COMMAND_AR}

echo "Installation successful"
echo "التثبيت بنجاح"