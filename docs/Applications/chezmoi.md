# Chezmoi

[link](https://dev.to/jerrynsh/a-brief-guide-to-manage-dotfiles-1h59)

To install

    pacman -sS chezmoi
    sudo pacman -S chezmoi


To add your .zshrc file which is typically located at our home directory, run:

    #This will copy ~/.zshrc to our source directory at ~/.local/share/chezmoi/dot_zshrc

    chezmoi add  ~/.zshrc

Here, you will see your .zshrc file as dot_zshrc.



To go to your source directory, simply run:

    chezmoi cd # Same as running cd ~/.local/share/chezmoi/dot_zshrc




1. Where to make changes

To modify the source state, you can either:

    Update the source state dotfile directly at ~/.local/share/chezmoi/dot_zshrc OR
    A quick way to do so is to use the chezmoi edit ~/.zshrc command

2. How to edit your dotfiles

Once you’re satisfied with your changes, save your dotfile and run:

    # To view the diff between ~/.local/share/chezmoi/dot_zshrc & ~/.zshrc
    chezmoi diff
    
    # To apply the changes to your original ~/.zshrc
    chezmoi -v apply

The apply command above will make changes to your original dotfile at your home directory, i.e. ~/.zshrc in this case.

