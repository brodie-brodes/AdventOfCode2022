def is_visible(trees, row, col):
    tree = int(trees[row][col])
    if row in [0, len(trees) - 1] or col in [0, len(trees[0]) - 1]:
        return True

    all_tree_lists = get_tree_view_lists(trees, row, col)

    return any([all([int(t) < tree for t in tree_list]) for tree_list in all_tree_lists])

def get_tree_view_lists(trees, row, col):

    left_trees = trees[row][:col]
    right_trees = trees[row][col+1:]
    above_trees = [r[col] for r in trees[:row]]
    below_trees = [r[col] for r in trees[row+1:]]

    return [left_trees, right_trees, above_trees, below_trees]

def get_view_score(tree_list, tree):
    view_score = 0
    for idx in range(len(tree_list)):
        view_score += 1
        if idx < len(tree_list) and tree_list[idx] >= tree:
            break
    
    return view_score

def get_scenic_score(trees, row, col):
    all_tree_lists = get_tree_view_lists(trees, row, col)
    left, right, above, below = [list(l) for l in all_tree_lists]

    left.reverse()
    above.reverse()

    scenic_score = 1
    for tree_list in [left, right, above, below]:
        
        scenic_score *= get_view_score(tree_list, trees[row][col])
    
    return scenic_score
        

    

def main():
    trees = [i.strip() for i in open("input.txt")]
    
    visible_trees = 0
    max_scenic_score = 0
    for row_idx, row in enumerate(trees):
        for col_idx, col in enumerate(trees[0]):
            
            if is_visible(trees, row_idx, col_idx):
                visible_trees += 1
            
            ss = get_scenic_score(trees, row_idx, col_idx)
            if ss > max_scenic_score:
                max_scenic_score = ss
    
    print("Total visible trees - ", visible_trees)
    print("Maximum scenic score - ", max_scenic_score)

if __name__ == "__main__":
    main()
