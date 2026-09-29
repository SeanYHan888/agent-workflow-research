# Upstream filename collision

At Grokking OOD revision `ba7927f641f2`, `example-codes/airline-management-system/java/` tracks both `README.md` and `readme.md` with different content. This Mac cannot store both names as separate files in the same directory. Git therefore reports the uppercase path modified after checkout; this is not a learner edit.

Both exact Git blobs are preserved here under distinct names: [uppercase original](README-uppercase.md) and [lowercase original](readme-lowercase.md). Their original relative links assume the upstream Java directory. The full originals also remain in Git. No upstream file was renamed, reset, hidden from status or committed. The selected OOAD/class/sequence readings are unaffected.
