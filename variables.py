
graph={
	'a':{'b':50,'c':80},
	'b':{'c':30,'d':20,'a':50},
	'c':{'d':60,'a':80,'b':30},
	'd':{'c':60,'b':20}
    # 'a':{'b':200,'c':400,'d':700},
    # 'b':{'c':100,'f':500},
    # 'c':{'f':600,'d':200},
    # 'd':{'e':300,'g':600},
    # 'e':{'g':300,'h':400},
    # 'f':{'e':100,'h':800},
    # 'g':{'h':200},
    # 'h':{'g':200},
}
# egde=[]
# traffic_lights_data={}
# for i in graph.keys():
# 	for j in graph[i].keys():
# 		egde.append(i+j)
# for i in egde:
# 	traffic_lights_data[i]=[10,'Red',120]
# print(traffic_lights_data)
traffic_lights_data={ 
    'ab':[10,'Red',820],'ac':[10,'Red',10],'ad':[10,'Red',10],'ae':[10,'Red',120],'af':[10,'Red',120],'ag':[10,'Red',120],'ah':[10,'Red',120],
	'ba':[10,'Red',120],'bc':[10,'Red',120],'bd':[10,'Red',10],'be':[10,'Red',120],'bf':[10,'Red',120],'bg':[10,'Red',120],'bh':[10,'Red',120],
	'ca':[10,'Red',120],'cb':[10,'Red',120],'cd':[10,'Red',120],'ce':[10,'Red',120],'cf':[10,'Red',120],'cg':[10,'Red',120],'ch':[10,'Red',120],
	'da':[10,'Red',120],'db':[10,'Red',120],'dc':[10,'Red',120],'de':[10,'Red',120],'df':[10,'Red',120],'dg':[10,'Red',120],'dh':[10,'Red',120],
	'ea':[10,'Red',120],'eb':[10,'Red',120],'ec':[10,'Red',120],'ed':[10,'Red',120],'ef':[10,'Red',120],'eh':[10,'Red',120],'eg':[10,'Red',120],
	'fa':[10,'Red',120],'fb':[10,'Red',120],'fc':[10,'Red',120],'fd':[10,'Red',120],'fe':[10,'Red',120],'fg':[10,'Red',120],'fh':[10,'Red',120],
	'ga':[10,'Red',120],'gb':[10,'Red',120],'gc':[10,'Red',120],'gd':[10,'Red',120],'ge':[10,'Red',120],'gf':[10,'Red',120],'gh':[10,'Red',120],
	'ha':[10,'Red',120],'hb':[10,'Red',120],'hc':[10,'Red',120],'hd':[10,'Red',120],'he':[10,'Red',120],'hf':[10,'Red',120],'hg':[10,'Red',120],
	}

# distance={
# 	'ab':200,
# 	'ac':400,
# 	'ad':700,
# 	'bc':100,
# 	'bf':500,
# 	'cf':600,
# 	'cd':200,
# 	'de':300,
# 	'dg':600,
# 	'eg':300,
# 	'eh':400,
# 	'fe':100,
# 	'fh':800,
# 	'gh':200
# }
def future_time_calc(instant_time,condition_of_light,time_cycle,time_to_reach_to_lights):
	for i in range(time_to_reach_to_lights):
		instant_time+=1
		if (instant_time>time_cycle):
			instant_time=instant_time%time_cycle
			if condition_of_light=='Red':
				condition_of_light='Green'
			else:
				condition_of_light='Red'
		
	returnvar=[instant_time,condition_of_light,time_cycle]
	return returnvar
# speed=10
# time_to_reach_to_lights=[]
# future_light_condition=[]
# traffic_lights_data_value1=[]
# traffic_lights_data_value2=[]
# for i in distance.values():
# 	time_to_reach_to_lights.append(i/speed)
# for i in traffic_lights_data.values():
#     traffic_lights_data_value1.append(i[0])
#     traffic_lights_data_value2.append(i[1])
# for i in range(len(time_to_reach_to_lights)):
#     future_light_condition.append(future_time_calc(traffic_lights_data_value1[i], 'Red',int(time_to_reach_to_lights[i])))

