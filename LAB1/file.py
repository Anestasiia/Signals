def write_to_file(N, b_k, delta):
    file = open("save_file.txt", "w")
    file.write("\nRank: " + str(N))
    file.write("\nCoefficients b_k:" + str(b_k))
    file.write("\nApproximation deviation: " + str(delta))
    file.close()