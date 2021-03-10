package test;

import java.util.*;

/*
 * 가사검색(트라이 자료구조)
 * 89일차에 파이썬으로 한것을 자바로 구현
 * 결과값은 나오나
 * 정확성: 0.0
 * 효율성: 0.0
 * 합계: 0.0 / 100.0
 */
public class _90_코딩문제_JAVA {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	
	
}

class Solution90 {
    public int[] solution(String[] words, String[] queries) {
    	Trie90 t=new Trie90();
    	Trie90 inv_t = new Trie90();
    	for(String word : words) {
    		t.insert(word);
    		inv_t.insert(new StringBuffer(word).reverse().toString());
    	}
        int[] answer = new int[queries.length];
        for(int i=0;i<queries.length;i++) {
        	String query=queries[i];
        	if(query.charAt(0)=='?') {
        		String chars=query.replace("?", "");
        		int check_length = query.length()-chars.length();
        		answer[i]=inv_t.search_count(chars, check_length);
        	}else {
        		String chars=query.replace("?", "");
        		int check_length = query.length()-chars.length();
        		answer[i]=t.search_count(chars, check_length);
        	}
        }
        return answer;
    }
}

class Node {
	String key;
	Map<String,Integer> remain_length;
	Map<String,Node> children;
	public Node(String key) {
		this.key=key;
		this.remain_length=new HashMap();
		this.children=new HashMap();
	}
}

class Trie90{
	Node head;
	public Trie90() {
		this.head=new Node(null);
	}
	
	public void insert(String str) {
		Node curr_node = this.head;
		
		int remain_length = str.length();
		if (curr_node.remain_length.containsKey(String.valueOf(remain_length))){
			curr_node.remain_length.put(String.valueOf(remain_length), curr_node.remain_length.get(String.valueOf(remain_length))+1);
		}else {
			curr_node.remain_length.put(String.valueOf(remain_length), 1);
		}
		
		for(String c : str.split("")) {
			if(!curr_node.children.containsKey(c)) {
				curr_node.children.put(c, new Node(c));
			}
			
			curr_node = curr_node.children.get(c);
			remain_length-=1;
			if (curr_node.remain_length.containsKey(String.valueOf(remain_length))) {
				curr_node.remain_length.put(String.valueOf(remain_length), curr_node.remain_length.get(String.valueOf(remain_length))+1);
			}else {
				curr_node.remain_length.put(String.valueOf(remain_length), 1);
			}
		}
	}
	
	public int search_count(String str,int check_length) {
		Node curr_node=this.head;
		
		if(!curr_node.remain_length.containsKey(String.valueOf(check_length+str.length()))) {
			return 0;
		}
		
		for(String c : str.split("")) {
			if(curr_node.children.containsKey(c)) {
				curr_node=curr_node.children.get(c);
			}else {
				return 0;
			}
		}
		
		if(curr_node.remain_length.containsKey(String.valueOf(check_length))) {
			return curr_node.remain_length.get(String.valueOf(check_length));
		}else {
			return 0;
		}
	}
}