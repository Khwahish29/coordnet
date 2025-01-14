import clsx from "clsx";
import { ChevronsRight } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router-dom";

import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { useNodesContext } from "@/hooks";
import useUser from "@/hooks/useUser";
import { cleanNodeTitle } from "@/lib/nodes";
import { BackendEntityType } from "@/types";

import ProfileDropdownButton from "./Profiles/ProfileDropdownButton";
import SpaceSidebar from "./Spaces/Sidebar";
import { Button } from "./ui/button";

const Header = ({ id, className }: { id: string; className?: string }) => {
  const { isGuest } = useUser();
  const { parent, nodes, breadcrumbs } = useNodesContext();
  const [sidebarOpen, setSidebarOpen] = useState<boolean>(false);

  const parentSpace = parent.type === BackendEntityType.SPACE ? parent.data : undefined;
  const parentMethod = parent.type === BackendEntityType.METHOD ? parent.data : undefined;

  const title = (parentSpace || parentMethod)?.title ?? "Untitled";

  return (
    <>
      <div className={clsx("flex h-6 items-center gap-2 px-3 text-sm", className)}>
        <div className="max-w-[220px] truncate">
          <Link
            to={`/${parent.type}s/${parent?.data?.id}`}
            className="font-normal text-neutral-500 hover:text-neutral-500 hover:underline"
          >
            {title}
          </Link>
        </div>
        {Boolean(breadcrumbs.length > 0) && <div className="">&raquo;</div>}
        {breadcrumbs.map((id, index) => (
          <div key={id} className="flex items-center gap-2">
            <div className="max-w-[220px] truncate">
              <Link
                to={`/${parent.type}s/${parent?.data?.id}/${id}`}
                className="font-normal text-neutral-500 hover:text-neutral-500 hover:underline"
              >
                {cleanNodeTitle(nodes.find((n) => n.id === id)?.title)}
              </Link>
            </div>
            {index < breadcrumbs.length - 1 && <div className="">&raquo;</div>}
          </div>
        ))}
        {breadcrumbs[breadcrumbs.length - 1] !== id &&
          ((parent.type === BackendEntityType.SPACE && id != parent?.data?.default_node) ||
            (parent.type === BackendEntityType.METHOD && id != parent?.data?.id)) && (
            <div className="flex items-center gap-2">
              <div className="">&raquo;</div>
              <div className="max-w-[220px] truncate">
                <Link
                  to={`/${parent.type}s/${parent?.data?.id}/${id}`}
                  className="font-normal text-neutral-500 hover:text-neutral-500 hover:underline"
                >
                  {cleanNodeTitle(nodes.find((n) => n.id === id)?.title)}
                </Link>
              </div>
            </div>
          )}
      </div>

      {isGuest ? (
        <></>
      ) : (
        <div className="absolute left-2 top-6 z-30 flex h-9 gap-2 leading-9">
          <Sheet open={sidebarOpen} onOpenChange={setSidebarOpen}>
            <SheetTrigger asChild>
              <Button variant="outline" className="size-9 p-0">
                <ChevronsRight strokeWidth={2.8} className="size-4 text-neutral-500" />
              </Button>
            </SheetTrigger>
            <SheetContent side="left" className="w-[320px] p-0">
              <SpaceSidebar open={sidebarOpen} />
            </SheetContent>
          </Sheet>
          <ProfileDropdownButton />
        </div>
      )}
    </>
  );
};

export default Header;
