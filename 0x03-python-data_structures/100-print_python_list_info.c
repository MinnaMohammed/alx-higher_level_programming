#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints info about Python lists
 * @p: PyObject pointer representing a Python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_length, i;
	PyObject *item;

	list_length = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", list_length);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < list_length; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
