# Customize

### Search Bar

#### Disable Bing search

You can remove all web search results by adding a key value to the Windows registry: 
```
HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer\DisableSearchBoxSuggestions set to a DWORD 32 value of 1.
```

I did it in HKEY_LOCAL_MACHINE it still worked

Create Key **"Explorer"** and create DWORD **"DisableSearchBoxSuggestions"**

Be sure to back up the registry using System Restore before you make changes.

