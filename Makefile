RAND := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')
DIR := workplace

randomize:
	find $(DIR)/user/src -name "*.c" | xargs sed -i 's/OK/OK$(RAND)/g'
	find check -name "*.py" | xargs sed -i 's/OK/OK$(RAND)/g'

test: randomize
	cp ../os/* $(DIR)/os/
	cp overwrite/Makefile $(DIR)/Makefile
ifeq ($(CHAPTER), 7)
	cp overwrite/Makefile-ch7 $(DIR)/Makefile
endif
ifeq ($(CHAPTER), 1)	
	echo `no ci for ch1`
else ifeq ($(CHAPTER), 2)
	echo `no ci for ch2`
else ifeq ($(CHAPTER), 3)
	make -C $(DIR) clean
	make -C $(DIR) test CHAPTER=3 BASE=0 | tee stdout-ch3
	python3 check/ch3.py < stdout-ch3

	make -C $(DIR) clean
	make -C $(DIR) test CHAPTER=3t BASE=0 | tee stdout-ch3t
	python3 check/ch3t.py < stdout-ch3t

else
	make -C $(DIR) clean
	make -C $(DIR) test CHAPTER=$(CHAPTER) BASE=0 | tee stdout-ch$(CHAPTER)
	python3 check/ch$(CHAPTER).py < stdout-ch$(CHAPTER)
endif

.PHONY: test
