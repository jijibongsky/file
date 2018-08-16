package newWord;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;


public class Tree {

	public Node root = new Node();
	static BufferedReader reader = null;
	int N = 3;
	int wordNumber = 100;
	double MI;

	public void generateForwardDic(String tempString) {
		char[] chs = tempString.toCharArray();
		for (int i = 0; i < chs.length; i++) {
			Map<Character, Node> cur = root.next;
			Node curNode = null;
			for (int j = 0; j < N && i + j < chs.length; j++) {
				int k = i + j;
				if (cur.containsKey(chs[k])) {
					curNode = cur.get(chs[k]);
					curNode.Upfre();
					cur = curNode.next;
//					System.out.println(curNode.ch);
//					System.out.println(curNode.fre);
				} else {
					Node addNode = new Node(chs[k]);
					cur.put(chs[k], addNode);
					addNode.father = curNode;
					curNode = addNode;
					curNode.Upfre();
					cur = addNode.next;
				}
			}
		}
//		System.out.println("Done");
	}

	public void generateForwardDic(File file) throws IOException {
		reader = new BufferedReader(new FileReader(file));
		String tempString = null;
		int line = 1;
		while ((tempString = reader.readLine()) != null && line < 100) {
			if (tempString.isEmpty()) {
				continue;
			}
			char[] chs = tempString.toCharArray();
			for (int i = 0; i < chs.length; i++) {
				Map<Character, Node> cur = root.next;
				Node curNode = null;
				for (int j = 0; j < N && i + j < chs.length; j++) {
					int k = i + j;
					if (cur.containsKey(chs[k])) {
						curNode = cur.get(chs[k]);
						curNode.Upfre();
						cur = curNode.next;
					} else {
						Node addNode = new Node(chs[k]);
						cur.put(chs[k], addNode);
						addNode.father = curNode;
						curNode = addNode;
						curNode.Upfre();
						cur = addNode.next;
					}
				}
			}
			line++;
		}
//		System.out.println("Done");
	}

	public int getFre(String tempString) {
		char[] chs = tempString.toCharArray();
		Map<Character, Node> cur = root.next;
		Node curNode = null;
		for (int i = 0; i < chs.length; i++) {
			if (cur.containsKey(chs[i])) {
				curNode = cur.get(chs[i]);
				cur = curNode.next;
			} else {
//				System.out.println(tempString + " 词频：" + 0);
				return 0;
			}
		}
//		System.out.println(tempString + " 词频：" + curNode.fre);
		return curNode.fre;
	}

	public double getRightEntropy(String tempString) {
		char[] chs = tempString.toCharArray();
		Map<Character, Node> cur = root.next;
		Node curNode = null;
		for (int i = 0; i < chs.length; i++) {
			if (cur.containsKey(chs[i])) {
				curNode = cur.get(chs[i]);
				cur = curNode.next;
			} else {
//				System.out.println(0);
				return 0;
			}
		}
		for (Character ch : cur.keySet()) {
			System.out.println(tempString + " 右邻接词：" + ch);
			System.out.println(tempString + " 右邻接词频：" + cur.get(ch).fre);
		}
		System.out.println(tempString + " 右邻接种数：" + cur.size());
		double entropy = 0;
		int sum = 0;
		int number = 0;
		for (Character ch : cur.keySet()) {
			number = cur.get(ch).fre;
			entropy += number * Math.log(number);
			sum += number;
		}
		if (sum == 0) {
//			System.out.println(tempString + " 右熵：" + 0);
			return 0;
		}
//		System.out.println(tempString + " 右熵：" + (Math.log(sum) - entropy/sum));
		return Math.log(sum) - entropy / sum;
	}

	public double getMI(String tempString) {
		if (tempString.length() <= 1) {
			System.out.println(tempString + " 互信息为：" + 0);
			return 0;
		}
		double coProbability = (double) getFre(tempString) / wordNumber;
		List<Double> mi = new ArrayList<Double>(tempString.length());
		for (int pos = 1; pos < tempString.length(); pos++) {
			String leftPart = tempString.substring(0, pos);
			String rightPart = tempString.substring(pos);
			double leftProbability = (double) getFre(leftPart) / wordNumber;
			double rightProbability = (double) getFre(rightPart) / wordNumber;
			mi.add(coProbability / (leftProbability * rightProbability));
		}
		MI = Collections.min(mi);
//		System.out.println(tempString + " 互信息为：" + MI);
		return MI;
	}

	public void depthOrderTraversal(Node node) {
		Map<Character, Node> cur = node.next;
		if (cur.size() == 0) {
			System.out.println("empty tree");
			return;
		}
//		System.out.print(cur.keySet()+"\n");
		ArrayDeque<Node> stack = new ArrayDeque<Node>();
		stack.push(node);
		while (stack.isEmpty() == false) {
			Node node1 = stack.pop();
			cur = node1.next;
//			System.out.print("当前节点：" + node1.ch + "    ");
			if(node1.father!=null) {
//				System.out.print("父节点：" + node1.father.ch + "    ");
			}else {
//				System.out.print("父节点为空："  + "    ");
			}
			for (Character ch : cur.keySet()) {
				stack.push(cur.get(ch));
			}
		}
		System.out.print("\n");
	}

}
