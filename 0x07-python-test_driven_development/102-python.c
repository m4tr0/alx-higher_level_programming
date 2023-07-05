#include <Python.h>

void print_python_string(PyObject *p) {
    Py_ssize_t length;
    Py_UNICODE *value;

    printf("[.] string object info\n");

    // Check if the object is a string
    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Get string length and value
    length = PyUnicode_GET_LENGTH(p);
    value = PyUnicode_AS_UNICODE(p);

    // Print string info
    printf("  type: %s\n", Py_TYPE(p)->tp_name);
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", value);
}
