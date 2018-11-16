#include <Python.h>

static PyObject* helloworld(PyObject* self, PyObject* args) 
{   
    printf("Hello World\n");
    return Py_None;
}

// Function Definition struct, NULL terminated.
static PyMethodDef methods[] = {
    { "helloworld", helloworld, METH_NOARGS, "Prints Hello World" },
    { NULL, NULL, 0, NULL }
};

// Module Definition struct.
static struct PyModuleDef demo = {
    PyModuleDef_HEAD_INIT,
    "demo",
    "Example Module",
    -1,
    methods
};


PyMODINIT_FUNC PyInit_demo(void)
{
    return PyModule_Create(&demo);
}