import argparse
from scipy import spatial
import heapq


def parse_args():
    '''
        Parses the arguments.
        '''
    parser = argparse.ArgumentParser(description="Run similarity.")
    parser.add_argument('--input', nargs='?', help="Input learned embeddings")
    parser.add_argument('--node', type=int, default=1, help='Input node id')
    parser.add_argument('--topK', type=int, default=5, help='Top K similar nodes')
    return parser.parse_args()


def read(filename):
    '''
    Read node2vec output embeddings into a structure
    '''
    features = {}
    with open(filename) as f:
        stat = f.readline().split(' ')
        for line in f:
            feat = [float(n) for n in line.strip().split(' ')]
            key = int(feat.pop(0))
            value = feat
            features[key] = value
    return {'numNodes': int(stat[0]), "numFeatures": int(stat[1]), "features": features}


def cosineSimilarity(feature, label, features, topK):
    results = {}
    for key in features.keys():
        if key != label:
            result = 1 - spatial.distance.cosine(feature, features[key])
            results[key] = result
    sortedByValue = heapq.nlargest(topK, results, key=results.get)
    return sortedByValue


def main(args):
    print("Similarity calculations")
    features = read(args.input)
    print("Features: " + str(features.get('numNodes')) + " , " + str(features.get('numFeatures')))
    print str(args.topK) + " similar nodes to node " + str(args.node)
    print cosineSimilarity(features.get("features").get(args.node), args.node, features.get("features"), args.topK)


if __name__ == '__main__':
    args = parse_args()
    main(args)


# uses:  python src/ml/similarity.py --input emb/karate.emb --node 1 --topK 5
