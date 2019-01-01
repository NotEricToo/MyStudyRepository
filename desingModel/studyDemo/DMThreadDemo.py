# 动态运行： 
# 使用线程， 循环运行： 

if __name__ == '__main__':
	t = threading.Thread(target=XXXClass().xxxfunction)
	t.setDaemon(true)
	t.start()


xxxfunction 中： 使用 循环 

	while loop_flag : 

		time.sleep(0.05)

		