//------------------------------------------------------
// STAMP FOLDINGS - Adapted to count for a given MV assignment
// USAGE: stamp_meander 0 (n) -> run all assignments for 1xn and output the counts one per line in lexicographic order (V = 0, M = 1)
// stamp_meander 1 (assignment) --> run this assignment and print the count
// Adapted from:   Joe Sawada, Roy Li
//------------------------------------------------------
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define MAX(a,b) ((a > b) ? a : b)
#define MAX_VAL 500
#define NULL -1

typedef struct List {
    int head, tail;
} List;

typedef struct Interval {
    int left, right, prev, next, node_ptr, next_perm, prev_perm;
} Interval;

typedef struct Node {
    List L, R;
    int up_interval;
    char up_side;
} Node;

//--------------------------------------------------------------------------------
// GLOBAL VARIABLES
//--------------------------------------------------------------------------------
Interval interval[MAX_VAL];
List perm;
Node node[MAX_VAL];
int N, MV, total=0;
char assignment[MAX_VAL];

//--------------------------------------------------------------------------------
int Input() {
    printf("ENTER gridlength n: ");
    scanf("%d", &N);
    printf("ENTER MV assignment (ex. MVMV): ");
    scanf("%s", assignment);
    int i;
    for (i = 0; i < MAX_VAL; i++) if (assignment[i] != 'M' && assignment[i] != 'V') break;
//    printf("%d", i);
    if (i != N-1) {
        printf("ERROR. MV assignment is not of length N-1.");
        return 1;
    }
    return 0;
}
//--------------------------------------------------------------------------------
void Print() {
    int i, j=0, one=0, a[MAX_VAL];

    i=perm.head;
    while(i != NULL) {
        a[++j] = interval[i].right;
        if (a[j] == 1) one = 1;
        i = interval[i].next_perm;
    }
    for (j=1; j<=N; j++) {
        if (a[j] < N-a[N-j+1]+1) break;
    }

//    for (j=1; j<=N; j++) printf("%d ", a[j]);
//    printf("\n");
    total++;
}
//--------------------------------------------------------------------------------
void InsertInterval(List *list, int t, int left, int right, int p, int n, int node_ptr) {

    if (p != NULL) interval[p].next = t;
    else list->head = t;

    if (n != NULL) interval[n].prev = t;
    else list->tail = t;

    interval[t].left = left;
    interval[t].right = right;
    interval[t].prev = p;
    interval[t].next = n;
    interval[t].node_ptr = node_ptr;
}

void RemoveInterval(List *list, int t) {

    if (interval[t].next == NULL) list->tail = interval[t].prev;
    else interval[interval[t].next].prev = NULL;

    if (interval[t].prev == NULL) list->head = interval[t].next;
    else interval[interval[t].prev].next = NULL;
}

void MoveInterval(int t, List *list1, List *list2, int p, int n, int node_ptr) {

    RemoveInterval(list1, t);
    InsertInterval(list2, t, interval[t].left, interval[t].right, p, n, node_ptr);
}
//--------------------------------------------------------------------------------
void SetNode(int t, int up_interval, int up_side) {

    node[t].up_interval = up_interval;
    node[t].up_side = up_side;
}

void SetNodeLists(int t, int left_head, int left_tail, int right_head, int right_tail) {

    if (left_head == NULL || left_tail == NULL) left_head = left_tail =  NULL;
    if (right_head == NULL || right_tail == NULL) right_head = right_tail = NULL;

    node[t].L.head = left_head;
    node[t].L.tail = left_tail;
    node[t].R.head = right_head;
    node[t].R.tail=  right_tail;
}
//--------------------------------------------------------------------------------
void UpdatePerm(int t,int i) {
    int p, n;

    p = interval[i].prev_perm;
    n = interval[i].next_perm;

    interval[2*t-1].prev_perm = p;
    interval[2*t-1].next_perm = 2*t;
    interval[2*t].prev_perm = 2*t-1;
    interval[2*t].next_perm = n;

    if (p != NULL) interval[p].next_perm = 2*t-1;
    else perm.head = 2*t-1;
    if (n != NULL) interval[n].prev_perm = 2*t;
}

void RestorePerm(int t,int i) {
    int p, n;

    p = interval[i].prev_perm;
    n = interval[i].next_perm;

    if (p != NULL) interval[p].next_perm = i;
    else perm.head = i;
    if (n != NULL) interval[n].prev_perm = i;
}
//--------------------------------------------------------------------------------
void Gen(int t, Node* X, int depth) {
    Node *Y;
    int i, up, j, n, p, old_up_side, old_up_interval, side, k;

    if (t > N) Print();
    else {
        // THIS IS THE MODIFICATION WE MADE

        side = 1;
        if (t % 2 == 0 && assignment[t-2] == 'V' || t % 2 == 1 && assignment[t-2] == 'M') {
            side = 2;
        }

        // VISIT LEFT LIST, THEN RIGHT LIST
//        for (side=1; side<=2; side++) {


            up = 0;
            if (side == 1) i = X->L.head;
            else  i = X->R.head;

            // VISIT ALL INTERVALS IN LIST
            while (i != NULL) {

                n = interval[i].next;
                p = interval[i].prev;
                j = interval[i].node_ptr;
                Y = &node[j];

                old_up_interval = Y->up_interval;
                old_up_side = Y->up_side;

                SetNode(2*t-1, -1,-1);
                SetNode(2*t, -1,-1);

                // UPDATE NEXT NODE and CREATE 2 NEW NODES
                if (side == 1) {
                    if (depth == 0 && i == X->L.head) {
                        up = 1;
                        if (Y->L.head != NULL) SetNodeLists(j, NULL, NULL, Y->L.head, Y->L.tail);
                        MoveInterval(X->R.tail, &X->R, &Y->R, Y->R.tail, NULL, 2*t-1);
                    }
                    else if (X->up_interval == i)  {
                        up = 1;
                    }
                    else if (up == 1 ||  X->up_side == 'r') {
                        SetNode(j, 2*t-1, 'l');
                        SetNode(2*t-1, X->up_interval, X->up_side);
                    }
                    else {
                        SetNode(j, 2*t, 'r');
                        SetNode(2*t, X->up_interval, 'r');
                    }
                    SetNodeLists(2*t-1, X->L.head, p, X->R.head, X->R.tail);
                    SetNodeLists(2*t, NULL, NULL, n, X->L.tail);
                }
                else {
                    if (depth == 0 && i == X->R.tail)  {
                        up = 1;
                        if (Y->R.head != NULL) SetNodeLists(j, Y->R.head, Y->R.tail, NULL, NULL);
                        MoveInterval(X->L.head, &X->L, &Y->L, NULL, Y->L.head, 2*t);
                    }
                    else if (X->up_interval == i)  {
                        up = 1;
                    }
                    else if (up == 1) {
                        SetNode(j, 2*t-1, 'l');
                        SetNode(2*t-1, X->up_interval, 'l');
                    }
                    else {
                        SetNode(j, 2*t, 'r');
                        SetNode(2*t, X->up_interval, X->up_side);
                    }
                    SetNodeLists(2*t-1, X->R.head, p, NULL, NULL);
                    SetNodeLists(2*t, X->L.head, X->L.tail, n, X->R.tail);
                }

                // INSERT NEW INTERVALS
                InsertInterval(&Y->L, 2*t-1, interval[i].left, t, Y->L.tail, NULL, 2*t-1);
                InsertInterval(&Y->R, 2*t, t, interval[i].right, NULL, Y->R.head, 2*t);

                // REMOVE CURRENT INTERVAL
                if (n != NULL) interval[n].prev = NULL;
                if (p != NULL) interval[p].next = NULL;

                // UPDATE THE PERMUTATION
                UpdatePerm(t,i);

                // MAKE RECURSIVE CALLS
                if (depth == 0 && (i== X->R.tail || i == X->L.head)) Gen(t+1, Y, 0);
                else if (X->up_interval == i)  Gen(t+1, Y, MAX(0,depth-1));
                else Gen(t+1, Y, depth+1);

                // RESTORE DATA STRUCTURES
                RestorePerm(t,i);

                if (n != NULL) interval[n].prev = i;
                if (p != NULL) interval[p].next = i;

                RemoveInterval(&Y->L, 2*t-1);
                RemoveInterval(&Y->R, 2*t);

                SetNode(j, old_up_interval, old_up_side);

                if (depth == 0) {
                    if (i == X->L.head) MoveInterval(Y->R.tail, &Y->R, &X->R, X->R.tail, NULL, j);
                    if (i == X->R.tail) MoveInterval(Y->L.head, &Y->L, &X->L, NULL, X->L.head, j);
                }

                i = n;	// NEXT INTERVAL
            }	}	}
//            }
//--------------------------------------------------------------------------------
int RunOnce() {
  int i,j;
  // INITIALIZE NODES
  for (i=0; i<=2*N; i++) {
      node[i].L.head = node[i].L.tail = NULL;
      node[i].R.head = node[i].R.tail = NULL;
      node[i].up_interval = NULL;
      node[i].up_side = '-';
  }

  SetNode(0, 2, 'r');
  InsertInterval(&node[0].L, 1, 0, 1, NULL, NULL, 2);
  InsertInterval(&node[0].R, 2, 1, MAX_VAL, NULL, NULL, 1);

  perm.head = 1;
  interval[1].prev_perm = NULL;
  interval[1].next_perm = 2;
  interval[2].prev_perm = 1;
  interval[2].next_perm = NULL;

  Gen(2, &node[0], 0);
  // printf("%s %d\n", assignment, total);
  printf("%d\n", total);
}

int RunAll() {
  for (int i = 0; i < (1 << (N-1)); i++){
    for (int j = 0; j < N-1; j++){
      if ((i & (1 << j)) >> j){
        assignment[j] = 'M';
      }
      else {
        assignment[j] = 'V';
      }
    }
    total = 0;
    RunOnce();
  }
}

int main(int argc, char *argv[]) {
    if (atoi(argv[1]) == 0) {
        N = atoi(argv[2]);
        RunAll();
    } else {
        for (N=0; N < MAX_VAL; N++) if (argv[2][N] != 'M' && argv[2][N] != 'V') break;
        N++;
        for (int i = 0; i < N-1; i++) {
            assignment[i] = argv[2][i];
        }
        RunOnce();
    }

    return 0;
}
