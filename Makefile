#!/usr/bin/env bash
# Variable
PROJECT := ya
COMMAND := ya

REMOVE_CMD := rm
MAKEDIR_CMD := mkdir
COPY_CMD := cp
RECURSIVE_FLAG := -r
RECURSIVE_FINAL_FLAG :=  -rf

.PHONY : install clean make_dir copy_dir move_cmd print_status

install: clean make_dir copy_dir move_cmd print_status

make_dir:
	@mkdir ${HOME}/${PROJECT}
	@mkdir ${HOME}/${PROJECT}/bin
	@mkdir ${HOME}/${PROJECT}/src

copy_dir:
	@cp -r bin/* ${HOME}/${PROJECT}/bin
	@cp -r src/* ${HOME}/${PROJECT}/src
	@cp start.py ${HOME}/${PROJECT}

# Adding class path
#export PATH=${HOME}/${PROJECT}/bin:$PATH

move_cmd:
	@mv ${HOME}/${PROJECT}/bin/cmd.sh ${HOME}/${PROJECT}/bin/${COMMAND}
	@chmod +x  ${HOME}/${PROJECT}/bin/${COMMAND}
	@ln ${HOME}/${PROJECT}/bin/${COMMAND} ${HOME}/${PROJECT}/bin/ي

print_status:
	@echo "Installation successful"
	@echo "التثبيت بنجاح"
	@echo "Next Add 'export PATH=${HOME}/${PROJECT}/bin:\$$PATH' to your .bash_profile or .bashrc"
	@echo " '.bash_profile أو .bashrc  إلى 'export PATH=${HOME}/${PROJECT}/bin:\$$PATH' التالي أضف"

clean:
	@rm -rf ${HOME}/${PROJECT}