#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    size = PyList_Size(p);
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *bytes;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
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

int main(void) {
    Py_Initialize();

    // Example usage
    PyObject *list_obj = PyList_New(3);
    PyList_SetItem(list_obj, 0, PyLong_FromLong(10));
    PyList_SetItem(list_obj, 1, PyBytes_FromString("Hello"));
    PyList_SetItem(list_obj, 2, PyFloat_FromDouble(3.14));

    print_python_list(list_obj);

    PyObject *bytes_obj = PyBytes_FromStringAndSize("example", 7);

    print_python_bytes(bytes_obj);

    Py_DECREF(list_obj);
    Py_DECREF(bytes_obj);

    Py_Finalize();

    return 0;
}
