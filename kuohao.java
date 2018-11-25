package ceshi;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class kuohao {

	public static Map<Integer, ArrayList<String>> treeLayer(String inputStr) {
		int len = inputStr.length();
		LinkedList<Integer> stack = new LinkedList<Integer>();
		Map<Integer, ArrayList<String>> layerDict = new HashMap<Integer, ArrayList<String>>();

		for (int i = 0; i < len; i++) {
			if (inputStr.charAt(i) == '(') {
				stack.push(i);
			} else if (inputStr.charAt(i) == ')') {
				if (stack.isEmpty()) {
					return null;
				} else {
//					System.out.println("第" + stack.size() + "层");
					int begin = stack.pop(); // stack.peek() 栈顶元素，不删除。

					ArrayList<String> g = layerDict.get(stack.size());
					if (g == null) {
						g = new ArrayList<String>();
						String tempstr = inputStr.substring(begin, i + 1);
						g.add(simple(tempstr));
						layerDict.put(stack.size(), g);
					} else {
						String tempstr = inputStr.substring(begin, i + 1);
						g.add(simple(tempstr));
					}
//					System.out.println("====" + begin + "和" + i + "配对");
//					System.out.println("====" + inputStr.substring(begin, i + 1));
//					System.out.println();
				}
			}
		}

		for (int key : layerDict.keySet()) {
			System.out.println(key + " " + layerDict.get(key));
		}
		// 循环结束后，栈空表示匹配完了，不空表示多余左括号
		if (stack.isEmpty()) {
			return layerDict;
		} else {
			return null;
		}
	}

	public static boolean match(String inputStr1, String inputStr2) {
		int len = inputStr1.length();
		for (int i = 1; i < len; i++) {
			if (inputStr1.charAt(i) == '(' | !isUpperLetter(inputStr1.charAt(i))) {
				return true;
			} else if (inputStr1.charAt(i) != inputStr2.charAt(i)) {
				System.out.println(inputStr1.charAt(i) + "  " + inputStr2.charAt(i));
				return false;
			}
		}
		return true;
	}

	public static String simple(String inputStr) {
		int len = inputStr.length();
		String Str = "";
		for (int i = 1; i < len; i++) {
			if (inputStr.charAt(i) == '(') {
				return Str;
			} else if (isUpperLetter(inputStr.charAt(i))) {
				Str += inputStr.charAt(i);
			}
		}
		return Str;
	}

	public static boolean isUpperLetter(char c) {
		if (c >= 'A' && c <= 'Z') {
			return true;
		}else {
			return false;
		}
	}


	public static void main(String[] args) {
		String inputStr = "(ROOT(IP(VP(ADVP(AD怎么))(VP(VV办理)(NP(NN移机))))))";
		inputStr = "(IP(VP(ADVP(AD怎么))(VP(VV办理)(NP(NN移机)))))";
//		inputStr = "(ROOT(IP(VP(ADVP(AD怎么)))))";
		inputStr = "(ROOT(IP(IP(VP(VV欢迎)(IP(VP(VV使用)(NP(NN中文)(NN分词))))))(PU，)(IP(PP(P在)(NP(PN这里)))(CP(ADVP(CS如果))(IP(NP(PN你))(VP(VV遇到)(NP(DP(DT什么))(NP(NN问题))))))(VP(ADVP(AD都))(VP(VV可以)(VP(VV联系)(NP(PN我))))))(PRN(IP(NP(NN，.我))(VP(ADVP(AD一定))(ADVP(AD尽我所能))(VP(VV帮助)(NP(PN大家))(IP(VP(ADVP(AD更快))(PU,)(ADVP(AD更准))(VP(VV更自由)(NP(NN!)))))))))))";
		
		System.out.println(treeLayer(inputStr));

//		System.out.println(match(("(VV欢迎)"), "(VV中文)"));
		
	}

}