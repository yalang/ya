#!/usr/bin/env bash
# Variable
PROJECT=ya
COMMAND=ya


# Removing existing installation
rm -rf $HOME/$PROJECT

# Creating directory
mkdir $HOME/$PROJECT
mkdir $HOME/$PROJECT/bin
mkdir $HOME/$PROJECT/src

# Copying file to the directory
cp -r bin/* $HOME/$PROJECT/bin
cp -r src/* $HOME/$PROJECT/src
cp start.py $HOME/$PROJECT

# Adding class path
#export PATH=$HOME/$PROJECT/bin:$PATH

# Renaming command file
mv $HOME/$PROJECT/bin/cmd.sh $HOME/$PROJECT/bin/$COMMAND
chmod +x  $HOME/$PROJECT/bin/$COMMAND
ln $HOME/$PROJECT/bin/$COMMAND $HOME/$PROJECT/bin/ي

echo "Installation successful"
echo "التثبيت بنجاح"
echo "Next Add 'export PATH=$HOME/$PROJECT/bin:\$PATH' to your .bash_profile or .bashrc"
echo " '.bash_profile أو .bashrc  إلى 'export PATH=$HOME/$PROJECT/bin:\$PATH' التالي أضف"