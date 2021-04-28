RAND := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')

randomize:
	find user/src -name "*.c" | xargs sed -i 's/OK/OK$(RAND)/g'
	find check -name "*.py" | xargs sed -i 's/OK/OK$(RAND)/g'

test: randomize
	cp overwrite/Makefile ../os/Makefile
	cp overwrite/pack.py ../os/pack.py
ifeq ($(CHAPTER), 5)
	sed -i 's/int id = get_id_by_name(.*)/int id = get_id_by_name("ch5_usertest")/g' ../os/loader.c
else ifeq ($(CHAPTER), 6)
	sed -i 's/int id = get_id_by_name(.*)/int id = get_id_by_name("ch6_usertest")/g' ../os/loader.c
else ifeq ($(CHAPTER), 7)
	sed -i 's/int id = get_id_by_name(.*)/int id = get_id_by_name("ch7_usertest")/g' ../os/loader.c
	cp overwrite/Makefile-ch7 ../os/Makefile
endif
ifeq ($(CHAPTER), 3)
	make -C user all CHAPTER=3_0
	make -C ../os clean
	make -C ../os run | tee stdout-ch3_0
	python3 check/ch3_0.py < stdout-ch3_0

	make -C user all CHAPTER=3_1
	make -C ../os clean
	make -C ../os run | tee stdout-ch3_1
	python3 check/ch3_1.py < stdout-ch3_1

	make -C user all CHAPTER=3_2
	make -C ../os clean
	make -C ../os run | tee stdout-ch3_2
	python3 check/ch3_2.py < stdout-ch3_2
else
	make -C user all CHAPTER=$(CHAPTER)
	make -C ../os clean
	make -C ../os run | tee stdout-ch$(CHAPTER)
	python3 check/ch$(CHAPTER).py < stdout-ch$(CHAPTER)
endif

.PHONY: test
