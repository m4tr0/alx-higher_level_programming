#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = PyList_Size(p);
	for (i = 0; i < size; i++)
{
	item = PyList_GetItem(p, i);
	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_list - Prints lists information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
{
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
    }

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes:", (size + 1 > 10 ? 10 : size + 1));
	bytes = PyBytes_AsString(p);
	for (i = 0; i < (size + 1 > 10 ? 10 : size + 1); i++)
	printf(" %02x", bytes[i] & 0xff);
	printf("\n");
}
