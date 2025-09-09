void indexsearch(int n, const keytype S[], keytype x, index& location)
{
    location = 0;
    while (location < n && S[location] != x)
        location++;
    if (location >= n)
        location = 0;
}