RAND := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')
DIR := workplace

# This is only for TAs to run base test, students do not know the token
TOKEN_SHA1 := $(shell echo -n '$(passwd)' | sha1sum | xargs | awk -F' ' '{ print $$1 }')
ifeq ($(TOKEN_SHA1), cb7997e364d3af0192a37edebaf166c0ecf10454)
	BASE := 1
	BASE_CHAR := b
else
	BASE := 0
# For students, report will be counted in to pass the CI
	ifeq ($(CHAPTER), 3)
		LAB := 1
	else ifeq ($(CHAPTER), 4)
		LAB := 2
	else ifeq ($(CHAPTER), 5)
		LAB := 3
	else ifeq ($(CHAPTER), 6)
		LAB := 4
	else ifeq ($(CHAPTER), 7)
# For ch7 we have no ch7_usertest, so just run ch7b_usertest to pass the CI
		BASE_CHAR := b
		LAB := 4
	else ifeq ($(CHAPTER), 8)
		LAB := 5
	endif
endif

randomize:
	find $(DIR)/user/src -name "*.c" | xargs -I {} sh -c 'sed -i.bak 's/OK/OK$(RAND)/g' {} && rm -rf {}.bak'
	find check -name "*.py" | xargs -I {} sh -c 'sed -i.bak 's/OK/OK$(RAND)/g' {} && rm -rf {}.bak'

test: randomize
	mkdir -p $(DIR)/os
	cp ../os/* $(DIR)/os/
	cp overwrite/Makefile $(DIR)/Makefile
ifeq ($(shell test $(CHAPTER) -ge 6; echo $$?),0)
	cp overwrite/Makefile-nfs $(DIR)/Makefile
	mkdir -p $(DIR)/nfs
	cp ../nfs/* $(DIR)/nfs/
endif
ifeq ($(CHAPTER), 1)
	echo `no ci for ch1`
else ifeq ($(CHAPTER), 2)
	echo `no ci for ch2`
else ifeq ($(CHAPTER), 5)
	make -C $(DIR) clean
	make -C $(DIR) test CHAPTER=5 BASE=$(BASE) INIT_PROC=ch5$(BASE_CHAR)_usertest | tee stdout-ch5
	python3 check/ch5$(BASE_CHAR).py < stdout-ch5

ifndef BASE
	make -C $(DIR) clean
	make -C $(DIR) test CHAPTER=5t BASE=0 INIT_PROC=ch5t_usertest | tee stdout-ch5t
	python3 check/ch5t.py < stdout-ch5 #t
endif

else
	make -C $(DIR) clean
	make -C $(DIR) test CHAPTER=$(CHAPTER) BASE=$(BASE) INIT_PROC=ch$(CHAPTER)$(BASE_CHAR)_usertest | tee stdout-ch$(CHAPTER)
	python3 check/ch$(CHAPTER)$(BASE_CHAR).py < stdout-ch$(CHAPTER)
endif

ifdef LAB
	@for i in $(shell seq $(LAB)); do \
	if ! [ -f ../reports/lab$$i.pdf -o -f ../reports/lab$$i.md ]; then \
		echo "Report for lab$$i needed. Add your report to reports/lab$$i.pdf or reports/lab$$i.md" ; \
		exit 1 ; \
	else \
		echo "Report for lab$$i found." ; \
	fi; \
	done
endif

.PHONY: test
