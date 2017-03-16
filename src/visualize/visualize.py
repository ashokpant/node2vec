#!/usr/bin/env python

from itertools import izip
import networkx as nx
import argparse
import pylab as plt


def parse_args():
    parser = argparse.ArgumentParser(description="Visualize the graph.")
    parser.add_argument('--input', nargs='?', help="Input edge list file")
    parser.add_argument('--labels', nargs='?', help="Input node labels file")
    return parser.parse_args()


def readLabels(filename):
    appendId = False
    labels = {}
    with open(filename) as f:
        for line in f:
            tokens = [n for n in line.strip().split()]
            key = int(tokens[0])
            if appendId:
                value = str(key) + ":" + str(tokens[2])
            else:
                value = tokens[2]

            labels[key] = value
    return labels


def main(args):
    labels = {}
    nodeSize = 100
    if args.labels is not None:
        nodeSize = 500
        labels = readLabels(args.labels)

    G = nx.read_edgelist(args.input, nodetype=int, data=(('weight',int),))
    # G = nx.read_edgelist(args.input, '#', None, None, int)
    pos = nx.spring_layout(G)
    if len(labels) == 0:
        labels = dict(izip(iter(pos.keys()), iter(pos.keys())))

    labels = dict((k,labels[k]) for k in pos.keys())  # retain labels that are in graph
    nx.draw_networkx_nodes(G, pos, None, nodeSize, 'g')
    nx.draw_networkx_edges(G, pos, width=3.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, labels, font_size=14)

    plt.axis('off')
    #plt.savefig("graph_with_labels.png")
    plt.show()


if __name__ == '__main__':
    args = parse_args()
    main(args)

    # uses: python src/visualize/visualize.py --input graph/karate.edgelist [ --labels graph/karate.labels ]
    # label file format
    # id1 label1
    # id2 label2
    # ... ...
