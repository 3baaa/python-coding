package test;

import java.util.*;

//트라이 자료구조
public class _88_코딩관련_JAVA {
	public static void main(String[] args) {
		Trie trie = new Trie();
		
		trie.insert("PI");
		trie.insert("PIE");
		trie.insert("POW");
		trie.insert("POP");
		
		System.out.println(trie.contains("POW"));
		System.out.println(trie.contains("PIES"));
	}
}

class TrieNode{
	private Map<Character,TrieNode> childNodes = new HashMap<>();
	private boolean isLastChar;
	
	
	public Map<Character, TrieNode> getChildNodes() {
		return childNodes;
	}
	
	public boolean isLastChar() {
		return isLastChar;
	}
	public void setLastChar(boolean isLastChar) {
		this.isLastChar = isLastChar;
	}
	
}

class Trie{
	private TrieNode rootNode;
	
	Trie(){
		rootNode = new TrieNode();
	}
	
	void insert(String word) {
		TrieNode thisNode = this.rootNode;
		for(int i=0;i<word.length();i++) {
			//thisNode = thisNode.getChildNodes().computeIfAbsent(word.charAt(i), c -> new TrieNode());
			
			if(!thisNode.getChildNodes().containsKey(word.charAt(i))){
				thisNode.getChildNodes().put(word.charAt(i), new TrieNode());
			}
			thisNode=thisNode.getChildNodes().get(word.charAt(i));
			
		}
		thisNode.setLastChar(true);
	}
	
	boolean contains(String word) {
		TrieNode thisNode =this.rootNode;
		for(int i=0;i<word.length();i++) {
			char character = word.charAt(i);
			TrieNode node =thisNode.getChildNodes().get(character);
			if(node == null) {
				return false;
			}
			
			thisNode=node;
		}
		
		return thisNode.isLastChar();
	}
	
	void delete(String word) {
		delete(this.rootNode,word,0);
	}
	
	private void delete(TrieNode thisNode,String word,int index) {
		char character = word.charAt(index);
		
		if(!thisNode.getChildNodes().containsKey(character)) {
			throw new Error("There is no["+word+"] in this Trie");
		}
		
		TrieNode childNode = thisNode.getChildNodes().get(character);
		index++;
		
		if(index==word.length()) {
			if(!childNode.isLastChar()) {
				throw new Error("There is no ["+word+"] in this Trie");
			}
			childNode.setLastChar(false);
			if(childNode.getChildNodes().isEmpty()) {
				thisNode.getChildNodes().remove(character);
			}
		}else {
			delete(childNode,word,index);
			
			if(!childNode.isLastChar() && childNode.getChildNodes().isEmpty()) {
				thisNode.getChildNodes().remove(character);
			}
		}
		
	}
}
