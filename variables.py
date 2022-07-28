
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
egde=[]
traffic_lights_data={}
for i in graph.keys():
	for j in graph[i].keys():
		egde.append(i+j)
for i in egde:
	traffic_lights_data[i]=[10,'Red']
# print(traffic_lights_data)
# traffic_lights_data={ 
#     'ab':[10,'Red'],
# 	'ac':[10,'Red'],
# 	'ad':[10,'Red'],
# 	'ae':[10,'Red'],
# 	'af':[10,'Red'],
# 	'ag':[10,'Red'],
# 	'ah':[10,'Red'],
# 	'ba':[10,'Red'],
# 	'bc':[10,'Red'],
# 	'bd':[10,'Red'],
# 	'be':[10,'Red'],
# 	'bf':[10,'Red'],
# 	'bg':[10,'Red'],
# 	'bh':[10,'Red'],
# 	'ca':[10,'Red'],
# 	'cb':[10,'Red'],
# 	'cd':[10,'Red'],
# 	'ce':[10,'Red'],
# 	'cf':[10,'Red'],
# 	'cg':[10,'Red'],
# 	'ch':[10,'Red'],
# 	'da':[10,'Red'],
# 	'db':[10,'Red'],
# 	'dc':[10,'Red'],
# 	'de':[10,'Red'],
# 	'df':[10,'Red'],
# 	'dg':[10,'Red'],
# 	'dh':[10,'Red'],
# 	'ea':[10,'Red'],
# 	'eb':[10,'Red'],
# 	'ec':[10,'Red'],
# 	'ed':[10,'Red'],
# 	'ef':[10,'Red'],
#     'eh':[10,'Red'],
# 	'eg':[10,'Red'],
# 	'fa':[10,'Red'],
# 	'fb':[10,'Red'],
# 	'fc':[10,'Red'],
# 	'fd':[10,'Red'],
# 	'fe':[10,'Red'],
# 	'fg':[10,'Red'],
# 	'fh':[10,'Red'],
# 	'ga':[10,'Red'],
# 	'gb':[10,'Red'],
# 	'gc':[10,'Red'],
# 	'gd':[10,'Red'],
# 	'ge':[10,'Red'],
# 	'gf':[10,'Red'],
# 	'gh':[10,'Red'],
# 	'ha':[10,'Red'],
# 	'hb':[10,'Red'],
# 	'hc':[10,'Red'],
# 	'hd':[10,'Red'],
# 	'he':[10,'Red'],
# 	'hf':[10,'Red'],
# 	'hg':[10,'Red'],}

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
def future_time_calc(instant_time,condition_of_light,time_to_reach_to_lights):
	for i in range(time_to_reach_to_lights):
		instant_time+=1
		if (instant_time>120):
			instant_time=instant_time%120
			if condition_of_light=='Red':
				condition_of_light='Green'
			else:
				condition_of_light='Red'
		
	returnvar=[instant_time,condition_of_light]
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

