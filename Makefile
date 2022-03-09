RAND := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')
DIR := workplace

randomize:
	find $(DIR)/user/src -name "*.c" | xargs sed -i 's/OK/OK$(RAND)/g'
	find check -name "*.py" | xargs sed -i 's/OK/OK$(RAND)/g'

test: randomize
	mkdir -p $(DIR)/os
	cp ../os/* $(DIR)/os/
	cp overwrite/Makefile $(DIR)/Makefile
ifeq ($(CHAPTER), 7)
	cp overwrite/Makefile-ch7 $(DIR)/Makefile
	mkdir -p $(DIR)/nfs
	cp ../nfs/* $(DIR)/nfs/
endif
ifeq ($(CHAPTER), 1)	
	echo `no ci for ch1`
else ifeq ($(CHAPTER), 2)
	echo `no ci for ch2`
else ifeq ($(CHAPTER), 5)
	make -C $(DIR) clean
	make -C $(DIR) test CHAPTER=5 BASE=0 | tee stdout-ch5
	python3 check/ch5.py < stdout-ch5

	make -C $(DIR) clean
	make -C $(DIR) test CHAPTER=5t BASE=0 | tee stdout-ch5t
	python3 check/ch5t.py < stdout-ch5t
else
	make -C $(DIR) clean
	make -C $(DIR) test CHAPTER=$(CHAPTER) BASE=0 INIT_PROC=ch$(CHAPTER)_usertest | tee stdout-ch$(CHAPTER)
	python3 check/ch$(CHAPTER).py < stdout-ch$(CHAPTER)
endif

.PHONY: test
