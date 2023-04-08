class Solution():
    def mergelink(self,link1,link2):
        if link1==None and link2==None:
            return None
        elif link1==None:
            return link2
        elif link2==None:
            return link1
        elif link1.val<link2.val:
            link1.next=self.mergelink(link1.next,link2)
        else:
            link2.next=self.mergelink(link1,link2.next)
            return