test:
	cp overwrite/Makefile ../os/Makefile
	cp overwrite/pack.py ../os/pack.py
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
