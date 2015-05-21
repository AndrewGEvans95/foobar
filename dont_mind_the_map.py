from itertools import product

class Subway:
    def __init__(data, stations, closed=None):
        data.stations = stations
        data.closed = closed
    def close(data, name):
        data.closed = name
    def subline(data):
        for i in range(1, data.numconnections() + 1):
            for p in product(range(data.numconnections()), repeat=i):
                yield p
    def numconnections(data):
        if data.stations:
            return len(data.stations[:1][0])
    def cont(data, position, station, line):
        destination = station[line]
        if destination == data.closed:
            destination = data.stations[data.closed][line]
        return destination if destination != data.closed else position
    def route(data, path, start):
    	position = start
        station = data.stations[start]
        for line in path:
            position = data.cont(position, station, line)
            station = data.stations[position]
        return position
    def __len__(data):
        return len(data.stations)
def runthrough(subway):
    def line_repeat(path):
        target = None
        for station in range(len(subway)):
            if station == subway.closed:
                continue
            destination = subway.route(path, station)
            if target is None:
                target = destination
            elif destination != target:
                return 0
    def line_exists():
        for path in subway.subline():
            if line_repeat(path) is not False:
                return 1
    if line_exists():
        return -1
    for station in range(len(subway)):
        subway.close(station)
        if line_exists():
            return station
    return -2

def answer(subway):
    return runthrough(Subway(subway))

print answer([[2, 1], [2, 0], [3, 1], [1, 0]])