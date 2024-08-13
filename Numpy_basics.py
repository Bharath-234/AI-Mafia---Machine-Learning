{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "654c7679-1c09-477c-8140-c0d34c957ad7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b1453867-6d40-44e2-915b-8057d573011a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b6a310a9-ac39-4758-a75c-2588799cd486",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([[1,2,3],[4,5,6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b801b246-9f3c-4037-be88-3b3360c5ffd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]]\n"
     ]
    }
   ],
   "source": [
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e261ec8d-5ba7-4d21-97db-4113c90c4468",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "numpy.ndarray"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "778bde58-69fc-4441-9110-f610d9190fdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(arr.ndim)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9e4a0a66-811d-4b9a-a3bb-78a16a6d48cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3)\n"
     ]
    }
   ],
   "source": [
    "print(arr.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "666d89c2-36d2-4d06-9c04-b136c37a1ec1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print(arr.size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4ae18c2f-fcfe-4a02-b02d-718ac86f6676",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int32\n"
     ]
    }
   ],
   "source": [
    "print(arr.dtype)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ff55790b-dd62-4de0-ac0e-37d704205764",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int32')"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "63c450c7-ead7-4d67-9bd7-35a151541cdb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d19a3374-913d-4225-a191-1db960bccb31",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.array([[1,2,3],[4,5,6],[7,8,9]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1d05bdbe-2337-4a9c-b0ca-0f18a2e00507",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 8, 9]])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c4ab494f-8514-4eb6-a75c-a13c4fed4fbc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "417ff5cb-311d-4a27-b327-004ddb3d1a9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 3)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6fca2952-d4ee-4a19-b1a2-8acee86ec71c",
   "metadata": {},
   "outputs": [],
   "source": [
    "c = np.zeros((3,4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "833c30fe-a396-4886-a4e4-ddf15ca847c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., 0.],\n",
       "       [0., 0., 0., 0.],\n",
       "       [0., 0., 0., 0.]])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2eadff29-e944-4cd8-9e5c-1f213605aae8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "28e4feaa-f351-4262-9774-d72f7eb61941",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 1., 1., 1.],\n",
       "       [1., 1., 1., 1.],\n",
       "       [1., 1., 1., 1.],\n",
       "       [1., 1., 1., 1.]])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.ones((4,4))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "304cc0fd-c1ec-4fbb-8388-247492b527cf",
   "metadata": {},
   "source": [
    "# np.eye(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "98326acd-57d1-4b0f-b579-45efe9cb4d6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  4,  8, 12, 16, 20, 24, 28])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(0, 30, 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "809ca9b8-9051-43d3-8738-c93ef0783a03",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0., 10., 20., 30.])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.linspace(0, 30, 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c449f861-88dc-4c30-9fc9-ef9b826bbc3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.        , 0.55555556, 1.11111111, 1.66666667, 2.22222222,\n",
       "       2.77777778, 3.33333333, 3.88888889, 4.44444444, 5.        ])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.linspace(0,5,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "a352be1f-7766-4a52-a0a0-dc0fcabb1c9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.array([[1,2,3,4],[4,5,6,5],[7,8,9,5]])\n",
    "new_arr = a.reshape((4,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "327139f9-311b-425e-8956-6db1820b5393",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 4, 5],\n",
       "       [6, 5, 7],\n",
       "       [8, 9, 5]])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "8baf9945-897f-4b64-ab2e-f7fe6e710223",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 4, 5, 6, 5, 7, 8, 9, 5])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr.flatten()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "a40c96ad-d1e5-439c-bd2c-519f184cd7f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[4, 4, 5],\n",
       "       [6, 5, 7],\n",
       "       [8, 9, 5]])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr[1:,:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "285de2f8-a26e-4842-b886-9139d98c14b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 4, 5],\n",
       "       [6, 5, 7],\n",
       "       [8, 9, 5]])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "ea1c40cc-bb29-4548-b196-4892b0b51256",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[6, 5, 7],\n",
       "       [8, 9, 5]])"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr[2:,:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "ca5a04f3-0a9c-44d8-a573-be47a51c3822",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [4, 4],\n",
       "       [6, 5],\n",
       "       [8, 9]])"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr[:,:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "9977ae4b-3d1f-4ea2-9107-845aef37e20a",
   "metadata": {},
   "outputs": [],
   "source": [
    "cond = new_arr>5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "5f397bfa-29b6-4084-a5ea-eef653366dfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[False, False, False],\n",
       "       [False, False, False],\n",
       "       [ True, False,  True],\n",
       "       [ True,  True, False]])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cond"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "ce5f87a8-6897-4a4a-ad64-a090318966c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 4, 5],\n",
       "       [6, 5, 7],\n",
       "       [8, 9, 5]])"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "7c92ea1d-3a45-4eb5-8925-588dbebef2b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 2,  3,  4],\n",
       "       [ 5,  5,  6],\n",
       "       [ 7,  6,  8],\n",
       "       [ 9, 10,  6]])"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e3192900-48c9-475f-b9cb-ae411e09158e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 1, 2],\n",
       "       [3, 3, 4],\n",
       "       [5, 4, 6],\n",
       "       [7, 8, 4]])"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "90675489-bc51-4076-be3a-d53efa37b611",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 4, 5],\n",
       "       [6, 5, 7],\n",
       "       [8, 9, 5]])"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "acafe624-4fb1-49e5-9124-e96ce578c9a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 3,  6,  9],\n",
       "       [12, 12, 15],\n",
       "       [18, 15, 21],\n",
       "       [24, 27, 15]])"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr*3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "505e4f5b-3389-4fce-8c87-0c7625be0e3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.5, 1. , 1.5],\n",
       "       [2. , 2. , 2.5],\n",
       "       [3. , 2.5, 3.5],\n",
       "       [4. , 4.5, 2.5]])"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "343e828b-22a7-4c58-97b4-e136bb0c0ee9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 6, 8],\n",
       "       [2, 4, 5, 9],\n",
       "       [3, 5, 7, 5]])"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "86ae04d2-7030-4dc7-abee-cd45f84ab729",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "d7843a84-6130-42c9-ad63-ed70240ed8f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 5, 7, 9])"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr.max(axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "46622570-e95a-48a6-89c1-4760718ecbb5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([8, 9, 7])"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr.max(axis = 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "4ea40444-db02-4518-beb8-054062958d30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 4, 5, 5])"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr.min(axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "24bc6f07-08af-4234-883b-3c712bd6241a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.sort(new_arr, axis = None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "903819f7-93b0-4914-9956-8aaa9c7e5a7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 4, 5],\n",
       "       [6, 5, 5],\n",
       "       [8, 9, 7]])"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.sort(new_arr, axis = 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "531dac66-9292-48a7-b857-c23dea6fa445",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 4, 5],\n",
       "       [5, 6, 7],\n",
       "       [5, 8, 9]])"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.sort(new_arr, axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "39b4642f-a749-415e-bc2a-55e75b9bd114",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 4, 5],\n",
       "       [6, 5, 5],\n",
       "       [8, 9, 7]])"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.sort(new_arr, axis = 0,kind = \"mergesort\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "dfeed5a0-f51e-4b07-a3ee-5e2f7249e9d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 4, 5],\n",
       "       [6, 5, 7],\n",
       "       [8, 9, 5]])"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "4f0d0fb8-c56b-479a-ba7a-ab78459ff18b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 4, 5],\n",
       "       [5, 6, 7],\n",
       "       [5, 8, 9]])"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.sort(new_arr, axis = 1,kind = \"mergesort\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "92e05b29-2a5f-4a3e-8752-c0612764b9f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "ar1 = np.array([[1,2],[2,3]])\n",
    "ar2 = np.array([[4,5],[6,7]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "3cd8db7d-b354-4701-bf25-c26dee8209c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [2, 3],\n",
       "       [4, 5],\n",
       "       [6, 7]])"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.vstack((ar1,ar2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "c8170756-c429-44fb-a53e-bfa954b277b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 4, 5],\n",
       "       [2, 3, 6, 7]])"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.hstack((ar1,ar2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "57ef38a2-a9ca-4419-add9-577ae5fc97ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [2, 3],\n",
       "       [4, 5],\n",
       "       [6, 7]])"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.row_stack((ar1,ar2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "bdf4ec63-6e91-4642-8cda-371b49a300c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr1 = np.column_stack((ar1,ar2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "6519607c-fe37-45c8-9c70-9e8d04c0084f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 4, 5],\n",
       "       [2, 3, 6, 7]])"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "52a71ba3-0485-41b8-975c-de69dee6eb08",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 4, 5])"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "f46942e3-d200-4ff9-b4cf-1abfcd9948c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 4, 5],\n",
       "       [2, 3, 6, 7]])"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.concatenate((ar1,ar2),1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "1ccd1c2c-017c-4f99-aa6c-13b4b4a20b20",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[array([[1, 2],\n",
       "        [2, 3]]),\n",
       " array([[4, 5],\n",
       "        [6, 7]])]"
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.hsplit(arr1,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "6f2c871b-3f4d-43c6-8db4-e2eddee4490c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 162,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.min(arr1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "a94b72c5-82e8-4482-93aa-4dcb0ae67073",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.max(arr1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "946eadd1-305b-4149-a1a3-56cfb3113055",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.75"
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(arr1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "dd6a36ac-27a3-4ddc-ba92-b6aaba120be7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.5"
      ]
     },
     "execution_count": 170,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.median(arr1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "92b63f71-3315-4bfd-9078-a8bbd3f554c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.75"
      ]
     },
     "execution_count": 176,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.average(arr1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47959fe6-5807-4e7b-ac52-355d506bf866",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
