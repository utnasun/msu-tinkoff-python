class Cluster:
    def __init__(self, number, length):
        self.upper = number + length
        self.lower = number - length
        self.numbers = [number]

    def check(self, number, length):
        if self.lower <= number <= self.upper:
            if number + length > self.upper:
                self.upper = number + length
            if number - length < self.lower:
                self.lower = number - length
            self.numbers.append(number)
            return True
        else:
            return False

    def num_sorted(self):
        return sorted(self.numbers)


class ClustersGroup:
    def __init__(self, first_cluster):
        self.clusters = [first_cluster]
        self.size = 1
        pass

    def add(self, cluster):
        self.size += 1
        self.clusters.append(cluster)

    def get_clusters(self):
        return self.clusters

    def get_size(self):
        return self.size


def write_to_file(filename, x: ClustersGroup):
    file = open(filename, "w")
    file.write(str(x.get_size()) + "\n")
    for cluster in x.clusters:
        i = 0
        while i != len(cluster.numbers) - 1:
            file.write(str(cluster.numbers[i]) + " ")
            i += 1
        file.write(str(cluster.numbers[i]) + "\n")
    file.close()
    pass

f = open('input.txt', 'r', encoding='utf-8')
text = f.readlines()
f.close()
L = int(text[0].split()[1])
nums = sorted([int(i) for i in text[1].split()])
temp = Cluster(nums[0], L)
clusters = ClustersGroup(temp)
for number in nums[1:]:
    flag = True
    for cluster in clusters.get_clusters():
        if cluster.check(number, L):
            flag = False
    if flag:
        temp = Cluster(number, L)
        clusters.add(temp)
write_to_file("output.txt", clusters)

