class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        // Swap left and right subtrees
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;

        // Recursively invert left and right subtrees
        invertTree(root->left);
        invertTree(root->right);

        return root;
    }
};
