import { HocuspocusProvider } from "@hocuspocus/provider";
import { createContext } from "react";
import * as Y from "yjs";

import { BackendNode, Space, SpaceNode } from "@/types";

type SpaceContextType = {
  space: Space | undefined;
  spaceError: Error | null;
  nodesMap: Y.Map<SpaceNode> | undefined;
  nodes: SpaceNode[];
  synced: boolean;
  connected: boolean;
  provider: HocuspocusProvider | undefined;
  deletedNodes: Y.Array<string> | undefined;
  backendNodes: BackendNode[];
  breadcrumbs: string[];
  setBreadcrumbs: React.Dispatch<React.SetStateAction<string[]>>;
};

/**
 * Context for sharing space between components
 */
export const SpaceContext = createContext<SpaceContextType | undefined>(undefined);
