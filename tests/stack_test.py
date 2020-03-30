import pytest
from gds import stack

def test_empty_stack():
	s = stack.Stack()
	assert s.is_empty()
	with pytest.raises(IndexError):
		s.pop()
	with pytest.raises(IndexError):
		s.peek()

def test_filo():
	s = stack.Stack()
	for i in range(10):
		s.push(i)
		assert not s.is_empty()
	for i in reversed(range(10)):
		assert not s.is_empty()
		assert s.peek() == i
		assert s.pop() == i
	assert s.is_empty()
	