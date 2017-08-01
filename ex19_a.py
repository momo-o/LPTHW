def time_for_playing(learning,eating,sleeping,others):
	time_for_playing=24-learning - eating - sleeping - others
	print "Time for playing today is %d." %time_for_playing


time_for_playing(2,2,8,3)